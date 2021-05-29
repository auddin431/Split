import React from "react";
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import InfoBar from '../InfoBar'
import IconButton from '@material-ui/core/IconButton';
import Button from '@material-ui/core/Button';
import AddIcon from '@material-ui/icons/Add';
import Logo from '../../images/logo.png'

import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import ListItemSecondaryAction from '@material-ui/core/ListItemSecondaryAction';
import Collapse from '@material-ui/core/Collapse';

import PlusIcon from '../../images/plus.svg'
import MinusIcon from '../../images/minus.svg'

const useStyles = makeStyles((theme) => ({
  root: {
    height: "42px",
    margin: "12px 0",
    padding: "9px 21px",
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
  },
  nested: {
    paddingLeft: theme.spacing(3),
  },
  actions: {
    display: 'flex',
    flexDirection: 'row',
  }
}));

const NestedList = (props) => {
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
        <ListItemText primary={props.itemName} secondary={props.cost}/>
        <ListItemSecondaryAction className={classes.actions}>
          <IconButton edge="end" onClick="">
            <img src={MinusIcon} alt="Minus sign inside circle."/>
          </IconButton>
          <Typography variant="h3" className={classes.quantity}>
            {props.quantity}
          </Typography>
          <IconButton edge="end" onClick="">
            <img src={PlusIcon} alt="Plus sign inside circle."/>
        </IconButton>
        </ListItemSecondaryAction>
      </ListItem>

      <Collapse in={open} timeout="auto" unmountOnExit>
        <List component="div" disablePadding>
          <ListItem button className={classes.nested}>
            <ListItemText primary={props.name} secondary={props.owed}/>
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

function testAPI() {
  fetch('/split_api/item_list')
  .then(response => response.json())
  .then(data => console.log(data));
}

const GroceryList = () => {
  testAPI()

  return (
    <>
      <InfoBar title="Grocery List" href="./chat" />
      <NestedList itemName="Apples" cost="2.99" name="First Last" owed="2.99"/>
      <Buttons />
    </>
  );
};

export default GroceryList;