import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Fab from "@material-ui/core/Fab";
import BottomNavigation from "@material-ui/core/BottomNavigation";
import BottomNavigationAction from "@material-ui/core/BottomNavigationAction";
import HomeIcon from "@material-ui/icons/Home";
import AccountIcon from "@material-ui/icons/Person";
import AddIcon from "@material-ui/icons/Add";

const useStyles = makeStyles({
  root: {
    position: "fixed",
    bottom: 0,
    height: "74px",
    width: "100vw",
    fontFamily: "'Koho', sans-serif",
    fontWeight: 600,
    fontSize: "16px",
    borderTop: "2px solid #C4C4C4",
  },
  fab: {
    bottom: "21px",
  },
});

const Navigation = (props) => {
  const classes = useStyles();

  return (
    <BottomNavigation value={props.page} showLabels className={classes.root}>
      <BottomNavigationAction
        label="Home"
        value="home"
        icon={<HomeIcon />}
        href="./home"
      />
      <Fab
        color="primary"
        aria-label="add"
        className={classes.fab}
        href="./chat"
      >
        <AddIcon />
      </Fab>
      <BottomNavigationAction
        label="Account"
        value="account"
        icon={<AccountIcon />}
        href="./account"
      />
    </BottomNavigation>
  );
};

export default Navigation;
