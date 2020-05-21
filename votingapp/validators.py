from django.core.exceptions import ValidationError


def validate_email(email):
    if not str(email).endswith('@stud.kpfu.ru'):
        raise ValidationError(
            (f'{email} is not a KFU email'),
            params={'email': email},
        )
