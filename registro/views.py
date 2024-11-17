import cv2
import os
from django.shortcuts import render, redirect
from .forms import FuncionarioForm, ColetaFacesForm
from .models import Funcionario, ColetaFaces
from django.http import StreamingHttpResponse
from registro.camera import VideoCamera

camera_detection = VideoCamera()  # Instância da classe VideoCamera

# Captura o frame com face detectada
def gen_detect_face(camera_detection):
    while True:
        frame = camera_detection.detect_face()  
        if frame is None:
            continue
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# Cria streaming para detecção facial
def face_detection(request):
    return StreamingHttpResponse(gen_detect_face(camera_detection),
                                 content_type='multipart/x-mixed-replace; \
                                     boundary=frame')


def criar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, request.FILES)
        if form.is_valid():
            funcionario = form.save()
            return redirect('criar_coleta_faces',
                            funcionario_id=funcionario.id)
    else:
        form = FuncionarioForm()
    return render(request, 'criar_funcionario.html', {'form': form})


# Cria uma função para extrair e retornar o file_path
def extract(camera_detection, funcionario_slug):
    amostra = 0 # Amostras inicial
    numeroAmostras = 10 # Numero de Amostra para extrair
    largura, altura = 220, 220  # largura, altura forma quadradinho
    file_paths = [] # lista de path das amostras 

    while amostra < numeroAmostras: # faz um loop até 10 amostra
        ret, frame = camera_detection.get_camera() # pega frame da camera (objeto atual)
        crop = camera_detection.sample_faces(frame)  # Captura as faces  

        if crop is not None: # se não for None, 
            amostra += 1 # conta 1 
            
            face = cv2.resize(crop, (largura, altura)) # resize 
            imagemCinza = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY) # Passa para cinza

            # Define o caminho da imagem
            file_name_path = f'./tmp/{funcionario_slug}_{amostra}.jpg' # exemplo> leticia_FUNC_XXXX_1.jpg
            cv2.imwrite(file_name_path, imagemCinza)
            file_paths.append(file_name_path) # Adiciona na lista
        else:
            print("Face não encontrada")

        if amostra >= numeroAmostras: 
            break # deu 10 amostra para

    camera_detection.restart()  # Reinicia a câmera após as capturas
    return file_paths


def face_extract(context, funcionario):
    num_coletas = ColetaFaces.objects.filter(
        funcionario__slug=funcionario.slug).count()
    
    print(num_coletas) # quantidade de imagens que funcionario tem cadastrado.
    
    if num_coletas >= 10: # Verifica se limte de coletas foi atingido
        context['erro'] = 'Limite máximo de coletas atingido.'
    else: 
        files_paths = extract(camera_detection, funcionario.slug) # passa camera e slug do funcionario
        print(files_paths) # Paths Rostos
        
        for path in files_paths:
            # Cria uma instância de ColetaFaces e salva a imagem
            coleta_face = ColetaFaces.objects.create(funcionario=funcionario)
            coleta_face.image.save(os.path.basename(path), open(path, 'rb'))
            os.remove(path)  # Remove o arquivo temporário após o salvamento

        # Atualiza o contexto com as coletas salvas
        context['file_paths'] = ColetaFaces.objects.filter(
            funcionario__slug=funcionario.slug)
        context['extracao_ok'] = True  # Define sinalizador de sucesso
        
          
    return context

# Cria coleta de faces (Registro)
def criar_coleta_faces(request, funcionario_id):
    print(funcionario_id)  # Identificador do funcionário cadastrado
    funcionario = Funcionario.objects.get(id=funcionario_id)  # Resgata o funcionário

    botao_clicado = request.GET.get('clicked', 'False') == 'True'
    
    context = {
        'funcionario': funcionario,  # Passa o objeto funcionario para o template
        'face_detection': face_detection, # passa camera aqui para renderizar no template
        'valor_botao': botao_clicado,
    }
    
    if botao_clicado:
        print("Cliquei em Extrair Imagens!")
        context = face_extract(context, funcionario)  # Chama a função de extração

    return render(request, 'criar_coleta_faces.html', context)



        