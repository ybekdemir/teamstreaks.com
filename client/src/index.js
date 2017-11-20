import React from 'react';
import ReactDOM from 'react-dom';
import 'bulma/css/bulma.css';
import './index.css';
import TeamStreaksTable from './components/TeamStreaksTable';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<TeamStreaksTable />, document.getElementById('root'));
registerServiceWorker();
