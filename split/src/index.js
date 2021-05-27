import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import Welcome from "./components/pages/Welcome";
import reportWebVitals from "./reportWebVitals";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

ReactDOM.render(
  <Router>
    <Switch>
      <Route path="/about">
        <App />
      </Route>
      <Route path="/welcome">
        <Welcome />
      </Route>
    </Switch>
  </Router>,
  document.getElementById("root")
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
