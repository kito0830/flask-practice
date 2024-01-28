from flask import (
  Blueprint, abort, render_template, redirect, url_for, flash, request
)
from flask_login import login_user, logout_user, login_required
from flaskr.models import User, PasswordResetToken
from flaskr import db
from os import path