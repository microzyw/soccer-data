from flask import Blueprint, render_template, jsonify, request, session
import math as math
from model.basic import login_required
from model.match import MatchModel

odds = Blueprint('odds', __name__)

@odds.route('/', methods=['GET'])
@login_required
def odds_index():
    return render_template('odds.html')

@odds.route('/showmatchlist', methods=['POST'])
@login_required
def odds_showmatchlist():
    page = int(request.form.get('page'))
    per = int(request.form.get('per'))
    nowDate = request.form.get('nowdate')
    sessionDate = session.get('ODDS_SHOW_MATCH_DATE')
    if nowDate == sessionDate:
        matchList = session.get('ODDS_SHOW_MATCH_LIST')
    else:
        matchList = MatchModel.getMatchListByDate(nowDate)
        session['ODDS_SHOW_MATCH_DATE'] = nowDate
        session['ODDS_SHOW_MATCH_LIST'] = matchList
    pageList = matchList[(page-1)*per:per*page:1]
    maxPage = math.ceil(len(matchList)/per)
    return jsonify({'success': 'true', 'matchlist': pageList, 'maxPage': maxPage})