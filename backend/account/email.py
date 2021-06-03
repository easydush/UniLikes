from djoser.email import ActivationEmail, PasswordResetEmail


class CustomActivationEmail(ActivationEmail):
    """
        Configuring activation template for djoser.
    """
    template_name = 'account/activation.html'


class CustomPasswordResetEmail(PasswordResetEmail):
    """
        Configuring password resetting template for djoser.
    """
    template_name = 'account/password_reset.html'
