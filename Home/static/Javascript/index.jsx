import React, {Component} from 'react';
import ReactDOM from 'react-dom';


class Page extends Component {
    constructor(props) {
        super(props);
        this.state = {
            section: null,
        };
    }

    render() {
        return (
            <div className="page-class">
                <p>Hey this is some text returned with a React Component!</p>
            </div>
        );
    }
}

/* Each Page component will consist of 1 or more Section components */
class Section extends Component {
    constructor(props) {
        super(props);
        this.state.src = {
            background: null,
        };
    }

    render () {
        return (
            <section className="main-section">
            <div className="main-image">
              <img id="banner"
              src={this.background} alt="Image Cannot be Displayed"/>
            </div>
          </section>
        );
    }
}


class NavBar extends Component {
    constructor(props) {
        super(props);
        this.props = {
            category: ["Portfolio", "Contact", "About"],
        }
    }

    render () {
        return (
            <span className="navigation-bar">
                <ul className="navigation-list">
                    {renderNavBarItem(this.category[0])}
                    {renderNavBarItem(this.category[1])}
                    {renderNavBarItem(this.category[2])}
                </ul>
            </span>
        );

        function renderNavBarItem() {
            return (
                <NavBarItem
                value={this.category}
            />
            );
        }
    }
}


class NavBarItem extends Component {

    render () {
        return (
            <li className="navigation-list-item">
                {this.state.value}
            </li>
        );
    }
}


ReactDOM.render(<Page />, document.getElementById('root'));