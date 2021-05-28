import React from "react";
import { makeStyles } from '@material-ui/core/styles';
import InfoBar from '../InfoBar'
import Button from '@material-ui/core/Button';
import ListIcon from '@material-ui/icons/List';
import Logo from '../../images/logo.png'

const useStyles = makeStyles(() => ({
  root: {
    height: "42px",
    margin: "12px 0",
    padding: "9px 21px",
    fontFamily: "'KoHo', sans-serif",
    fontWeight: 600,
    fontSize: "16px",
    textTransform: "capitalize",
    borderRadius: "25px",
  },
  buttons: {
    position: "fixed",
    bottom: "21px",
    margin: "0 auto",
    width: "100vw",
    display: "flex",
    justifyContent: "center",
  }
}));

const Buttons = () => {
  const classes = useStyles();

  return (
    <div className={classes.buttons}>
      <input
        type="file"
        accept="image/*" 
        capture="camera"
        style={{ display: 'none' }}
        id="photoInput"
      />
      <label htmlFor="photoInput">
        <Button 
          variant="contained" 
          color="primary" 
          className={classes.root}
          style={{ "marginRight": "12px" }}
          component="span"
        >
          <img 
            src={Logo} 
            alt="Split Logo"
            height="24px"
            style={{ "marginRight": "10px" }}
          />
          Scan & Split
        </Button>
      </label> 

      <Button 
        variant="outlined" 
        color="primary" 
        className={classes.root}
        startIcon={<ListIcon />}
        href="./list"
      >
        View List
      </Button>
    </div>
  );
};

const Chat = (props) => {
  return (
    <>
      <InfoBar 
        title={props.group ? props.group : "Roommates"} 
        href="./home" 
        image="true" 
        placeholder="true"/>
      <Buttons />
    </>
  );
};

export default Chat;