import React from 'react';

import StreakItem from './StreakItem';

const StreakList = ({ streaks, isLoading }) => {
  return (
    <table className="table is-striped is-fullwidth">
      <thead>
        {isLoading
          ? <tr>
            <th>Loading...</th>
          </tr>
          : <tr>
            <th>Team Name</th>
            <th>Streak</th>
          </tr>
        }
      </thead>
      <tbody>
        {streaks.map((streak, index) => <StreakItem key={streak._id} streak={streak} />)}
      </tbody>
    </table>
  );
}

export default StreakList;
