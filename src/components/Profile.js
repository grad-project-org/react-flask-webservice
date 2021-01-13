import React, { Component } from "react";
// import jwt_decode from "jwt-decode";

class Profile extends Component {
  render() {
    const { user, logOut } = this.props;

    return (
      <div className="text-center mt-4">
        <span className="text-secondary font-weight-bold pl-1">
          Welcome {user} here you will be able to take attendance from the
          stream by detecting each face!
        </span>
      </div>
    );
  }
}

export default Profile;
