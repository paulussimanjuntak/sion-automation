from flask import Blueprint, render_template
from services.resources.sion.form import SionForm

sions = Blueprint('sions',__name__)

@sions.route('/sion',methods=['GET','POST'])
def sion():
    form = SionForm()
    if form.validate_on_submit():
        print("nic3")
    return render_template('sion/sion.html',form=form)
