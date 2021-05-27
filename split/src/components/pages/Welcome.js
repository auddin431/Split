import React, { useState } from "react";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import { withStyles } from "@material-ui/core/styles";
import { Link } from "react-router-dom";
import "./Welcome.css";

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

const StyledTextField = withStyles({
  root: {
    color: "linear-gradient(45deg, #ff0000 30%, #ff0000 90%)",
  },
})(TextField);

const Welcome = () => {
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
    <>
      <div className="wrapper">
        <h1>Welcome to Split.</h1>
        <form noValidate autoComplete="off">
          <StyledTextField id="email" label="Email" onChange={emailHandler} />
          <StyledTextField
            id="pass"
            label="Password"
            onChange={passwordHandler}
          />
        </form>
      </div>
      <div className="wrapper">
        <StyledButton className="colorTest" variant="contained">
          Log In
        </StyledButton>
        <p style={{ textAlign: "center" }}>
          Don't have an account? <Link to="/register">Sign Up</Link>
        </p>
      </div>
    </>
  );
};

export default Welcome;
