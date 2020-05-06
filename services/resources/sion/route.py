from flask import Blueprint, render_template, url_for, redirect, flash
from services.resources.sion.form import SionForm
from services.libs.AutomationSion import AutomationSion

sions = Blueprint('sions',__name__)

@sions.route('/sion',methods=['GET','POST'])
def sion():
    form = SionForm()
    if form.validate_on_submit():
        nim = form.nim.data
        password = form.password.data
        harapan = [form.harapan.data]
        sion = AutomationSion(nim,password,harapan)
        if sion.automated() == 400: flash('Upps credential invalid or you already fill up kuesioner!','error')
        else: flash('Kuesioner berhasil di isi!','success')
        return redirect(url_for('sions.sion'))

    return render_template('sion/sion.html',form=form)
