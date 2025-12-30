from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def home(): return 'home'

@bp.route('/create')
def create_note(): return 'create note'

@bp.route('/read')
def read_note(): return 'read note'

@bp.route('/update')
def update_note(): return 'update note'

@bp.route('/delete')
def delete_note(): return 'delete note'