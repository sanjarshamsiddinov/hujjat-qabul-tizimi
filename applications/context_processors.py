from applications.models import Application


def staff_notifications(request):
    if request.user.is_authenticated and hasattr(request.user, 'staff_profile'):
        return {
            'unreviewed_count': Application.objects.filter(holat='yangi').count(),
        }
    return {}
