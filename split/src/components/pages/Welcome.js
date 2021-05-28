import React, { useState } from "react";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import { makeStyles, withStyles } from "@material-ui/core/styles";
import { Link } from "react-router-dom";
import "./Welcome.css";

const useStyles = makeStyles({
  root: {
    marginBottom: "18px",
  },
});

const StyledButton = withStyles({
  root: {
    height: "52px",
    margin: "12px 0",
    fontFamily: "'Koho', sans-serif",
    fontWeight: 600,
    fontSize: "16px",
  },
  label: {
    textTransform: "capitalize",
  },
})(Button);

const Welcome = () => {
  const classes = useStyles();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const emailHandler = (e) => {
    setEmail(e.target.value);
    console.log(e.target.value);
  };
  const passwordHandler = (e) => {
    setPassword(e.target.value);
  };
  
  return (
    <div className="wrapper">
        <h1 className="title">Welcome to Split.</h1>
        <form noValidate autoComplete="off">
          <TextField 
            id="email"
            className={classes.root}
            label="Email" 
            onChange={emailHandler} 
            fullWidth
          />
          <TextField
            id="pass"
            label="Password"
            type="password"
            onChange={passwordHandler}
            fullWidth
          />
        </form>
        <StyledButton variant="contained" color="primary">
          Log In
        </StyledButton>
        <p>
          Don't have an account? <Link className="action" to="/register">Sign Up.</Link>
        </p>
    </div>
  );
};

export default Welcome;
