from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE, verbose_name="Email")
    fullname = models.CharField(max_length=100, verbose_name="Full name")

    VIEWER = 'Viewer'
    EMPLOYEE = 'Employee'
    STATUS_CHOICES = [
        (VIEWER, 'Viewer'),
        (EMPLOYEE, 'Employee'),
    ]
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = "User Status"
        verbose_name_plural = "User Statuses"


class VacationRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateField(verbose_name="Start date")
    finish_date = models.DateField(verbose_name="Finish date")
    reason = models.TextField(
        max_length=1000, blank=True, verbose_name="Reason")

    WAITING = 'Waiting'
    APPROVED = 'Approved'
    REJECTED = 'Rejected'
    STATUS_CHOICES = [
        (WAITING, 'Waiting'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        default=WAITING,
    )

    class Meta:
        verbose_name = 'Vacation Request'

    def __str__(self):
        return f"Vacation Request for {self.user.email}"
