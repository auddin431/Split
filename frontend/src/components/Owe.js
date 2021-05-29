import React from "react";
import "./Owe.css";

const Owe = (props) => {
  return (
    <>
      <h2 className="wrapperText">Your Money</h2>
      <div className="box-container">
        <div className="box">
          <div>
            You Owe
            <br />
            <b>${props.owe}</b>
          </div>
        </div>
        <div className="box">
          <div>
            You're Owed
            <br />
            <b>${props.owed}</b>
          </div>
        </div>
      </div>
    </>
  );
};

export default Owe;
