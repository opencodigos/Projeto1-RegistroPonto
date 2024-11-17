from django.shortcuts import render, redirect
from .forms import FuncionarioForm, ColetaFacesForm
from .models import Funcionario, ColetaFaces
from django.http import StreamingHttpResponse
from registro.camera import VideoCamera

camera_detection = VideoCamera()  # Instância da classe VideoCamera

# Captura o frame com face detectada
def gen_detect_face(camera_detection):
    while True:
        frame = camera_detection.get_camera()  
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


# Cria coleta de faces (Registro)
def criar_coleta_faces(request, funcionario_id):
    print(funcionario_id)  # Identificador do funcionário cadastrado
    funcionario = Funcionario.objects.get(id=funcionario_id)  # Resgata o funcionário

    context = {
        'funcionario': funcionario,  # Passa o objeto funcionario para o template
        'face_detection': face_detection, # passa camera aqui para renderizar no template
    }

    return render(request, 'criar_coleta_faces.html', context)

