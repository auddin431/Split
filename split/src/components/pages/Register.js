import React, { useState } from "react";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import { withStyles } from "@material-ui/core/styles";
import { Link } from "react-router-dom";

const StyledButton = withStyles({
  root: {
    background: "linear-gradient(45deg, #000 30%, #000 90%)",
    borderRadius: 3,
    border: 0,
    color: "white",
    height: 48,
    padding: "0 30px",
  },
  label: {
    textTransform: "capitalize",
  },
})(Button);

const nameHandler = () => {
  return;
};
const emailHandler = () => {
  return;
};
const passwordHandler = () => {
  return;
};
const numberHandler = () => {
  return;
};

const Register = () => {
  return (
    <>
      <div className="wrapper">
        <h1>Join the family.</h1>
        <form noValidate autoComplete="off">
          <TextField id="full name" label="full name" onChange={nameHandler} />
          <TextField id="email" label="email" onChange={emailHandler} />
          <TextField
            id="password"
            label="password"
            type="password"
            onChange={passwordHandler}
          />
          <TextField id="number" label="number" onChange={numberHandler} />
        </form>
      </div>
      <div className="wrapper">
        <StyledButton className="colorTest" variant="contained">
          Register
        </StyledButton>
        <p style={{ textAlign: "center" }}>
          Already have an account? <Link to="/welcome">Log In</Link>
        </p>
      </div>
    </>
  );
};

export default Register;
