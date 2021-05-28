import Owe from "../Owe";
import { Helmet } from "react-helmet";
import "./Home.css";
import React from "react";
import Navigation from "../Navigation"

const Home = () => {
  return (
    <React.Fragment>
      <Helmet>
        <style>{"body { background-color: black; }"}</style>
      </Helmet>
      <div className="wrapperBackground">
        <Owe owe="128.37" owed="40.59" />
      </div>
      <div
        style={{
          backgroundColor: "white",
          borderRadius: "25px",
          height: "70vh",
        }}
      ></div>
      <Navigation page="home"/>
    </React.Fragment>
  );
};

export default Home;