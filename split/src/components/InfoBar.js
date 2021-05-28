import React from "react";
import { makeStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import Typography from '@material-ui/core/Typography';
import BackIcon from '@material-ui/icons/KeyboardBackspace';

const useStyles = makeStyles(() => ({
  backButton: {
    marginRight: "3px",
  },
  title: {
    fontFamily: "'Koho', sans-serif",
    fontWeight: 600,
  },
  image: {
    height: "24px",
    borderRadius: "50%",
  },
  placeholder: {
    backgroundColor: "white",
    height: "24px",
    width: "24px",
    borderRadius: "50%",
    marginRight: "12px",
  }
}));

const InfoBar = (props) => {
  const classes = useStyles();

  return (
    <AppBar position="static">
      <Toolbar>
        <IconButton
          edge="start" 
          className={classes.backButton} 
          color="inherit" 
          aria-label="back"
          href={props.href}
        >
          <BackIcon />
        </IconButton>
        {props.image ? (props.placeholder ? <div className={classes.placeholder}></div> :
          <img src={props.image} alt="Group" className={classes.image} />) : <></>
        }
        <Typography variant="h6" className={classes.title}>
          {props.title}
        </Typography>
        {props.action ? <Button color="inherit">{props.action}</Button> : <></>}
      </Toolbar>
    </AppBar>
  );
};

export default InfoBar;