from pydantic import BaseModel, Field

from helpers.locators import (
    LOGIN_BRANDING_CONTAINER_CLASS,
    LOGIN_BRANDING_LOGO_CSS,
    LOGIN_SOCIAL_ICONS_CLASS,
    RESET_PASSWORD_REQUIRED_MESSAGE_CSS,
    RESET_PASSWORD_SUCCESS_TITLE_CSS,
)


class LoginUser(BaseModel):
    username: str
    password: str


class ResetPasswordRequest(BaseModel):
    username: str


class UiElementCollection(BaseModel):
    name: str
    class_name: str
    minimum_count: int = Field(ge=1)


class VisibleUiElementExpectation(BaseModel):
    name: str
    selector_type: str
    selector_value: str
    minimum_count: int = Field(default=1, ge=1)


class PresentUiElementExpectation(BaseModel):
    name: str
    selector_type: str
    selector_value: str
    minimum_count: int = Field(default=1, ge=1)


admin_user = LoginUser(
    username="Admin",
    password="admin123",)


reset_password_request_user = ResetPasswordRequest(
    username="Admin",)


login_social_icons = UiElementCollection(
    name="Login social icons",
    class_name=LOGIN_SOCIAL_ICONS_CLASS,
    minimum_count=4,)


login_branding_container = VisibleUiElementExpectation(
    name="Login branding container",
    selector_type="class",
    selector_value=LOGIN_BRANDING_CONTAINER_CLASS,)


login_branding_logo = PresentUiElementExpectation(
    name="OrangeHRM logo image",
    selector_type="css",
    selector_value=LOGIN_BRANDING_LOGO_CSS,)


reset_password_required_message = VisibleUiElementExpectation(
    name="Reset password required message",
    selector_type="css",
    selector_value=RESET_PASSWORD_REQUIRED_MESSAGE_CSS,)


reset_password_success_title = VisibleUiElementExpectation(
    name="Reset password success title",
    selector_type="css",
    selector_value=RESET_PASSWORD_SUCCESS_TITLE_CSS,)
