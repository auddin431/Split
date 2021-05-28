import React, { useState } from "react";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import { makeStyles, withStyles } from "@material-ui/core/styles";
import { Link } from "react-router-dom";

const useStyles = makeStyles({
  root: {
    marginBottom: "18px",
  },
});

const StyledButton = withStyles({
  root: {
    background: "linear-gradient(45deg, #000 30%, #000 90%)",
    borderRadius: 3,
    border: 0,
    color: "white",
    height: 48,
    padding: "0 30px",
    margin: "12px 0",
    fontFamily: "'Koho', sans-serif",
    fontWeight: 600,
    fontSize: "16px",
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
  const classes = useStyles();

  return (
      <div className="wrapper">
        <h1 className="title">Join the family.</h1>
        <form noValidate autoComplete="off">
          <TextField 
            id="name" 
            className={classes.root}
            label="Full Name" 
            onChange={nameHandler} 
            fullWidth
          />
          <TextField 
            id="email" 
            className={classes.root}
            label="Email" 
            onChange={emailHandler} 
            fullWidth
          />
          <TextField
            id="password"
            className={classes.root}
            label="Password"
            type="password"
            onChange={passwordHandler}
            fullWidth
          />
          <TextField 
            id="number" 
            label="Phone Number" 
            onChange={numberHandler} 
            fullWidth
          />
        </form>
        <StyledButton variant="contained">
          Register
        </StyledButton>
        <p>
          Already have an account? <Link className="action" to="/welcome">Log In.</Link>
        </p>
      </div>
  );
};

export default Register;
