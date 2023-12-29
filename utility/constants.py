from django.db import models
from django.utils.translation import gettext_lazy as _


# Page  Options
class PageType(models.IntegerChoices):
    PRIVACY_POLICY = 0, _("Privacy Policy")
    TERMS_AND_CONDITION = 1, _("Terms and Condition")
    ABOUT_US = 2, _("About Us")
    GENERAL = 3, _("General")