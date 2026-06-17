from pydantic import BaseModel, Field


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
    class_name="oxd-icon orangehrm-sm-icon",
    minimum_count=4,)


login_branding_container = VisibleUiElementExpectation(
    name="Login branding container",
    selector_type="class",
    selector_value="orangehrm-login-branding",)


login_branding_logo = PresentUiElementExpectation(
    name="OrangeHRM logo image",
    selector_type="css",
    selector_value='img[alt="orangehrm-logo"]',)


reset_password_required_message = VisibleUiElementExpectation(
    name="Reset password required message",
    selector_type="css",
    selector_value=(
        "#app > div.orangehrm-forgot-password-container > "
        "div.orangehrm-forgot-password-wrapper > div > form > "
        "div.oxd-form-row > div > span"
    ),)


reset_password_success_title = VisibleUiElementExpectation(
    name="Reset password success title",
    selector_type="css",
    selector_value=".orangehrm-forgot-password-title",)
