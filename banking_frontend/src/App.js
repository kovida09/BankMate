import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Chat from './components/Chat';
import Sidebar from './components/Sidebar';
import Dashboard from './components/Dashboard';
import ChatInterface from './components/ChatInterface';
import './App.css';
import AccountInformation from './components/AccountInformation';
import TransactionInformation from './components/TransactionInformation';
import LoanInformation from './components/LoanInformation';
import CreditCardInformation from './components/CreditCardInformation';
import CustomerInformation from './components/customerInformation';


function App() {
  return (
    <Router>
      
      <Switch>
        <Route path="/coustomer-information" component={CustomerInformation} />
        <Route path="/account-information" component={AccountInformation} />
        <Route path="/transaction-information" component={TransactionInformation} />
        <Route path="/loan-information" component={LoanInformation} />
        <Route path="/credit-card-information" component={CreditCardInformation} />
        <Route path="/chat" component={Chat} />
      </Switch>
    </Router>
  );
}

export default App;
