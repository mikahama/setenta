from django.conf.urls import patterns, include, url

from setenta_members import views

urlpatterns = patterns('',
    url(r'^$', views.root_redir, name="root_page"),
    url("index", views.index, name="index"),
    url("validate", views.send_email_key, name="validate"),
    url("mail_sent", views.mail_sent, name="mail_sent"),
    url("show_captcha", views.captcha_view, name="captcha"),
    url("check_captcha", views.check_captcha, name="check_captcha"),
    url("login", views.login, name="login"),
    url("logout", views.logout, name="logout"),
    url("failed", views.login_failed, name="login_failed"),
    url("edit_profile", views.edit_profile, name="edit_profile"),
    url("update_profile", views.update_profile, name="update_profile"),
    url("update_complete", views.update_complete, name="update_complete"),
    url("admin", views.admin_login, name="admin_login"),
    url("logad", views.admin_check, name="admin_check"),
    url("member_list", views.member_list, name="member_list"),
    url("password", views.change_password, name="password"),
)
