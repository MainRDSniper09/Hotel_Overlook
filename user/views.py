from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.utils.html import format_html

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Customers')
            user.groups.add(group)
            return redirect('user-login')
    else:
        form = CreateUserForm()
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)


def profile(request):
    context = {

    }
    return render(request, 'user/profile.html', context)


def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('user-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'user/profile_update.html', context)

# Envio de Correos
from django.core.mail import EmailMultiAlternatives
from django.utils.html import format_html

def contact_us(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if name and email and message:
            subject = f"📨 Nuevo Mensaje de {name} - Hotel Overlook"
            
            body_text = f"""
            Nombre: {name}
            Correo: {email}
            
            Mensaje:
            {message}
            """

            body_html = format_html(f"""
                <html>
                <body style="background-color: #f4f4f4; padding: 20px; font-family: 'Arial', sans-serif;">
                    <div style="max-width: 600px; margin: 0 auto; background: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1);">
                        <div style="text-align: center; border-bottom: 3px solid #007bff; padding-bottom: 10px;">
                            <h2 style="color: #333; margin: 0;">📨 Nuevo Mensaje de Contacto</h2>
                            <p style="color: #555; font-size: 14px;">Hotel Overlook</p>
                        </div>
                        
                        <div style="padding: 20px;">
                            <p><strong style="color: #007bff;">Nombre:</strong> {name}</p>
                            <p><strong style="color: #007bff;">Correo:</strong> {email}</p>
                            <p><strong style="color: #007bff;">Mensaje:</strong></p>
                            <div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-style: italic; color: #555;">
                                {message}
                            </div>
                        </div>

                        <div style="text-align: center; margin-top: 20px;">
                            <a href="http://127.0.0.1:8000/" style="background: #007bff; color: #ffffff; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">Visitar Hotel Overlook</a>
                        </div>

                        <div style="border-top: 3px solid #007bff; padding-top: 10px; margin-top: 20px; text-align: center; font-size: 12px; color: #777;">
                            <p>📍 Hotel Overlook - Contacto</p>
                            <p>Este es un mensaje automático, por favor no responda a este correo.</p>
                        </div>
                    </div>
                </body>
                </html>
            """)

            try:
                email_message = EmailMultiAlternatives(
                    subject,
                    body_text,  # Texto en caso de que el cliente no soporte HTML
                    "barretosanchez6@gmail.com",  # Emisor
                    [email],  # Receptor
                )
                email_message.attach_alternative(body_html, "text/html")
                email_message.send()

                messages.success(request, "¡Tu mensaje ha sido enviado correctamente!")
            except Exception as e:
                messages.error(request, f"Error al enviar correo: {str(e)}")
            
            return redirect("contact_us")
        else:
            messages.error(request, "Por favor, completa todos los campos.")

    return render(request, "contact_us/contact_us.html")
