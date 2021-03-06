import {
  requestPending,
  requestSuccess,
  requestFailed,
} from "../../utils/helpers/request";

const initialState = {
  me: null,
  error: null,
  status: "INIT",
};

export const authReducer = function (state = initialState, action) {
  switch (action.type) {
    case requestPending("SIGN_UP"):
      return {
        ...state,
        status: requestPending("SIGN_UP"),
      };
    case requestSuccess("SIGN_UP"):
      return {
        ...state,
        status: requestSuccess("SIGN_UP"),
      };
    case requestFailed("SIGN_UP"):
      return {
        ...state,
        status: requestFailed("SIGN_UP"),
        error: action.payload,
      };
    case requestPending("SIGN_IN"):
      return {
        ...state,
        status: requestPending("SIGN_IN"),
      };
    case requestSuccess("SIGN_IN"):
      return {
        ...state,
        status: requestSuccess("SIGN_IN"),
      };
    case requestFailed("SIGN_IN"):
      return {
        ...state,
        status: requestFailed("SIGN_IN"),
        error: action.payload,
      };
    case "SET_USER_INFO":
      return {
        ...state,
        me: action.payload,
      };
    case "REMOVE_USER":
      return {
        ...state,
        me: null,
        error: null,
        status: "INIT",
      };
    default:
      return state;
  }
};
