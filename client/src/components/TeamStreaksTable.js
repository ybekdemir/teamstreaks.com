import React, { Component } from 'react';
import axios from 'axios';

import CategorySelections from './CategorySelections';
import StreakList from './StreakList';

class TeamStreaksTable extends Component {
  constructor(props) {
    super(props);
    this.state = {
      streakTypes: [],
      tournaments: [{ caption: 'All', id: 0 }],
      selStreakType: 0,
      selTournament: 0,
      streaks: [],
      isLoading: true
    }

    this.apiUrl = 'https://damp-meadow-47784.herokuapp.com/api/';
  }

  async componentDidMount() {
    const streakTypesReq = await axios.get(this.apiUrl + 'data/bettypes');
    const tournamentsReq = await axios.get(this.apiUrl + 'data/tournaments');
    const streaksReq = (streakTypesReq.data && streakTypesReq.data.streaktypes.length > 0)
      ? await axios.get(this.apiUrl + 'streak/' + streakTypesReq.data.streaktypes[0].uid)
      : {};

    this.setState({
      streakTypes: streakTypesReq.data.streaktypes,
      tournaments: this.state.tournaments.concat(tournamentsReq.data),
      selStreakType: (streakTypesReq.data && streakTypesReq.data.streaktypes.length > 0) ? streakTypesReq.data.streaktypes[0].uid : 0,
      selTournament: 0,
      streaks: streaksReq.data,
      isLoading: false
    });
  }

  setLoadingState = () => {
    this.setState({
      ...this.state,
      streaks: [],
      isLoading: true
    });
  }

  handleTournamentChange = (e) => {
    this.setLoadingState();
    const tournamentId = Number(e.target.value);
    const s = this.state;
    axios.get(this.apiUrl + 'streak/' + s.selStreakType + (tournamentId > 0 ? '/' + tournamentId : ''))
      .then(res => {
        this.setState({
          ...s,
          selTournament: tournamentId,
          streaks: res.data,
          isLoading: false
        });
      });
  }

  handleStreakChange = (e) => {
    this.setLoadingState();
    const streakTypeId = Number(e.target.value);
    const s = this.state;
    axios.get(this.apiUrl + 'streak/' + streakTypeId + (s.selTournament > 0 ? '/' + s.selTournament : ''))
      .then(res => {
        this.setState({
          ...s,
          selStreakType: streakTypeId,
          streaks: res.data,
          isLoading: false
        });
      });
  }

  render() {
    const s = this.state;
    return (
      <section className="hero is-light is-fullheight">
        <div className="hero-head">
          <div className="container">
            <div className="columns is-centered">
              <div className="column is-half is-one-third-widescreen">

                <div className="box" style={{margin: '15px 10px'}}>
                  <CategorySelections
                    streakTypes={s.streakTypes}
                    tournaments={s.tournaments}
                    streakTypeSelection={s.selStreakType}
                    tournamentSelection={s.selTournament}
                    onStreakTypeChange={this.handleStreakChange}
                    onTournamentChange={this.handleTournamentChange} />

                  <hr />
                  
                  <StreakList streaks={s.streaks} isLoading={s.isLoading} />
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    );
  }
}

export default TeamStreaksTable;
