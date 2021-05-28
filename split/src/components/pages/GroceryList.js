import React from "react";
import { makeStyles } from '@material-ui/core/styles';
import InfoBar from '../InfoBar'
import Button from '@material-ui/core/Button';
import AddIcon from '@material-ui/icons/Add';
import Logo from '../../images/logo.png'

import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import Collapse from '@material-ui/core/Collapse';
import ExpandLess from '@material-ui/icons/ExpandLess';
import ExpandMore from '@material-ui/icons/ExpandMore';

const useStyles = makeStyles((theme) => ({
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
  },
  list: {
    width: '100%',
    maxWidth: 360,
    backgroundColor: theme.palette.background.paper,
    fontFamily: "'KoHo', sans-serif",
  },
  nested: {
    paddingLeft: theme.spacing(3),
  },
}));

const NestedList = () => {
  const classes = useStyles();
  const [open, setOpen] = React.useState(true);

  const handleClick = () => {
    setOpen(!open);
  };

  return (
    <List
      component="nav"
      className={classes.list}
    >
      <ListItem button onClick={handleClick}>
        <ListItemText primary="Sent mail" secondary="Details"/>
        {open ? <ExpandLess /> : <ExpandMore />}
      </ListItem>

      <Collapse in={open} timeout="auto" unmountOnExit>
        <List component="div" disablePadding>
          <ListItem button className={classes.nested}>
            <ListItemText primary="Starred" secondary="Details"/>
          </ListItem>
        </List>
      </Collapse>

      <ListItem button onClick={handleClick}>
        <ListItemText primary="Inbox" secondary="Details"/>
        {open ? <ExpandLess /> : <ExpandMore />}
      </ListItem>

      <Collapse in={open} timeout="auto" unmountOnExit>
        <List component="div" disablePadding>
          <ListItem button className={classes.nested}>
            <ListItemText primary="Starred" secondary="Details"/>
          </ListItem>
        </List>
      </Collapse>
    </List>
  );
};

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
        startIcon={<AddIcon />}
      >
        Add Item
      </Button>
    </div>
  );
};

const GroceryList = () => {
  return (
    <>
      <InfoBar title="Grocery List" href="./chat" />
      <NestedList />
      <Buttons />
    </>
  );
};

export default GroceryList;