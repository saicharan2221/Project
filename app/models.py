# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from datetime import datetime 
from django.db import models
from django.utils.timezone import now


class AppUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    access_label = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_user'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class Designation(models.Model):
    desg_id = models.AutoField(primary_key=True)
    desg_name = models.CharField(max_length=45, blank=True, null=True)
    desg_description = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'designation'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EmpDetails(models.Model):
    emp_details_id = models.AutoField(primary_key=True)
    date_of_joining = models.DateField(blank=True, null=True)
    status_of_emp = models.CharField(max_length=30, blank=True, null=True)
    desg = models.ForeignKey(Designation, models.DO_NOTHING, blank=True, null=True)
    dept = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)
    project = models.CharField(max_length=45, blank=True, null=True)
    user = models.ForeignKey(AppUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emp_details'


class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    contact = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(AppUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class LeaveApplication(models.Model):
    application_id = models.AutoField(primary_key=True)
    date_of_application = models.DateField(default=now()) 
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    leave_approval_date = models.DateField(blank=True, null=True)
    leave_status = models.CharField(max_length=15, blank=True, null=True)
    user = models.ForeignKey(AppUser, models.DO_NOTHING, blank=True, null=True)
    leave_description = models.CharField(max_length=200, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'leave_application'


class LeaveType(models.Model):
    leavetype_id = models.AutoField(primary_key=True)
    leave_name = models.CharField(max_length=45, blank=True, null=True)
    leave_desc = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leave_type'


class Leaves(models.Model):
    leaves_consumed = models.IntegerField(blank=True, null=True)
    leaves_remaining = models.IntegerField(blank=True, null=True)
    total_leaves = models.IntegerField(blank=True, null=True)
    leave_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(AppUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leaves'
