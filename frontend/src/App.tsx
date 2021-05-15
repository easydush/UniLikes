import React from 'react';
import { Routes as R } from './constants';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { Login, Main, Register } from './pages';
import { PrivateRoute } from './components/PrivateRoute';
import 'antd/dist/antd.css';

function App(): JSX.Element {
    return (
        <Router>
            <Switch>
                <Route exact component={Login} path={R.LOGIN} />
                <Route exact component={Register} path={R.REGISTER} />
                <PrivateRoute exact component={Main} path={R.ROOT} />
                <PrivateRoute exact component={Main} path={R.MAIN} />
            </Switch>
        </Router>
    );
}

export default App;
