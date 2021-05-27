import React, { useState } from "react";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import { withStyles } from "@material-ui/core/styles";
import "./Welcome.css";

const StyledButton = withStyles({
  root: {
    background: "black",
    borderRadius: 3,
    border: 0,
    color: "white",
    height: 48,
    padding: "0 30px",
    "&:active": {
      backgroundColor: "black",
      color: "white",
    },
  },
  label: {
    textTransform: "capitalize",
  },
  hover: {
    background: "white",
  },
})(Button);

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
    <div className="wrapper">
      <h1>Welcome to Split.</h1>
      <form noValidate autoComplete="off">
        <TextField id="email" label="Email" onChange={emailHandler} />
        <TextField id="pass" label="Password" onChange={passwordHandler} />
      </form>
      <StyledButton variant="contained">Log In</StyledButton>
    </div>
  );
};

export default Welcome;
