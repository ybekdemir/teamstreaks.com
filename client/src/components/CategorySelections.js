import React from 'react';

const CategorySelections = (props) => {
  return (
    <div>
    <div className="field is-horizontal">
      <div className="field-label is-normal">
        <label className="label">StreakTypes</label>
      </div>
      <div className="field-body">
        <div className="field">
          <div className="control">
            <div className="select is-fullwidth">
              <select value={props.streakTypeSelection} onChange={props.onStreakTypeChange}>
                {props.streakTypes.map((sT, index) => <option key={sT.uid} value={sT.uid}>{sT.name}</option>)}
              </select>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div className="field is-horizontal">
      <div className="field-label is-normal">
        <label className="label">Tournament</label>
      </div>
      <div className="field-body">
        <div className="field">
          <div className="control">
            <div className="select is-fullwidth">
              <select value={props.tournamentSelection} onChange={props.onTournamentChange}>
                {props.tournaments.map((t, index) => <option key={t.id} value={t.id}>{t.caption}</option>)}
              </select>
            </div>
          </div>
        </div>
      </div>
    </div>
    </div>
  );
}

export default CategorySelections;
