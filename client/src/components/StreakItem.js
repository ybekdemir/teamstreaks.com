import React from 'react';

const StreakItem = ({streak}) => (
  <tr>
    <td>{streak.team_name}</td>
    <td>{streak.count}</td>
  </tr>
);

export default StreakItem;
