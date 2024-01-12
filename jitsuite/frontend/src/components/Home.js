import React ,{ Component } from "react";
import JoinPage from "./join";
import {
    BrowserRouter as Router,
    Routes,
    Route
  } from "react-router-dom";

export default class HomePage extends Component {
    constructor(props){
        super(props)
    }

    render() {
     return (
        <Router>
            <Routes>
                <Route path="/" caseSensitive={false}  element={ <JoinPage /> } />
                <Route path="/join" caseSensitive={false}  element={ <JoinPage /> } />
            </Routes>
        </Router>
     );
    }
}