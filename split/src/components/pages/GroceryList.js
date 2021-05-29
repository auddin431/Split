import React, { useEffect } from "react";
import { makeStyles } from "@material-ui/core/styles";
import Typography from "@material-ui/core/Typography";
import InfoBar from "../InfoBar";
import IconButton from "@material-ui/core/IconButton";
import Button from "@material-ui/core/Button";
import AddIcon from "@material-ui/icons/Add";
import Logo from "../../images/logo.png";

import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemText from "@material-ui/core/ListItemText";
import ListItemSecondaryAction from "@material-ui/core/ListItemSecondaryAction";
import Collapse from "@material-ui/core/Collapse";
import DeleteIcon from "@material-ui/icons/Delete";

import PlusIcon from "../../images/plus.svg";
import MinusIcon from "../../images/minus.svg";

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
    width: "100%",
    fontFamily: "'KoHo', sans-serif",
  },
  nested: {
    paddingLeft: theme.spacing(3),
  },
}));

const NestedList = (props) => {
  const classes = useStyles();
  const [open, setOpen] = React.useState(false);

  const handleClick = () => {
    setOpen(!open);
  };

  return (
    <List component="nav" className={classes.list}>
      <ListItem button onClick={handleClick}>
        <ListItemText primary={props.itemName} secondary={props.quantity} />
        <ListItemSecondaryAction>
          <IconButton edge="end" onClick="">
            <img src={MinusIcon} alt="Minus sign inside circle." />
          </IconButton>
          <IconButton edge="end" onClick="">
            <img src={PlusIcon} alt="Plus sign inside circle." />
          </IconButton>
        </ListItemSecondaryAction>
      </ListItem>

      <Collapse in={open} timeout="auto" unmountOnExit>
        <List component="div" disablePadding>
          {props.people.map((person) => {
            return (
              <ListItem button className={classes.nested}>
                <ListItemText primary={person.name} secondary={person.q} />
              </ListItem>
            );
          })}
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
        style={{ display: "none" }}
        id="photoInput"
      />
      <label htmlFor="photoInput">
        <Button
          variant="contained"
          color="primary"
          className={classes.root}
          style={{ marginRight: "12px" }}
          component="span"
        >
          <img
            src={Logo}
            alt="Split Logo"
            height="24px"
            style={{ marginRight: "10px" }}
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
  const bananas = [{ name: "Sam", q: 2 }];
  const cherrios = [{ name: "Bill", q: 3 }];
  const milk = [{ name: "Bill", q: 2 }];
  const lunchables = [
    { name: "Sam", q: 2 },
    { name: "Bill", q: 3 },
    { name: "Sarah", q: 5 },
  ];
  const hershey = [
    { name: "Sam", q: 2 },
    { name: "Bill", q: 2 },
    { name: "Sarah", q: 2 },
  ];
  const user1_params = {
    username: "Sam",
    password: "abhi",
  };

  const user2_params = {
    username: "Bill",
    password: "abhi",
  };

  const user3_params = {
    username: "Sarah",
    password: "abhi",
  };

  const prefix = "http://localhost:5000/split_api/";

  const addUsers = async () => {
    const response = await fetch("/split_api/user/create", {
      method: "POST",
      body: JSON.stringify({
        username: "Abdul",
        password: "abhi",
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
    const content = await response.json();
    console.log(content);
  };

  const check = async () => {
    const response = await fetch("/split_api/item_list");
    const r = await response.json();
    console.log(response);
  };

  useEffect(() => {
    console.log("Hello world");
    addUsers();
    //check();
  }, []);
  return (
    <>
      <InfoBar title="Grocery List" href="./chat" />
      <NestedList itemName="Bananas" quantity="2" people={bananas} />
      <NestedList itemName="Cherrios" quantity="3" people={cherrios} />
      <NestedList itemName="Milk" quantity="2" people={milk} />
      <NestedList itemName="Lunchables" quantity="1" people={lunchables} />
      <NestedList itemName="Hershey" quantity="6" people={bananas} />
      <Buttons />
    </>
  );
};

export default GroceryList;
