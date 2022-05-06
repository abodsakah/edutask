describe("user case R8UC1", () => {
    describe('Logging into the system', () => {
        before(function () {
            // create a fabricated user from a fixture
            cy.visit("localhost:3000")
            cy.fixture('user.json')
                .then((user) => {
                    cy.request({
                        method: 'POST',
                        url: 'http://localhost:5000/users/create',
                        form: true,
                        body: user
                    }).then((response) => {
                        this.uid = response.body._id.$oid
                    })
                })
        })

        it('starting out on the landing screen', () => {
            // make sure the landing page contains a header with "login"
            cy.get('h1')
                .should('contain.text', 'Login')
        })

        it('login to the system with an existing account', () => {
            // detect a div which contains "Email Address", find the input and type
            // declarative
            cy.contains('div', 'Email Address')
                .find('input[type=text]')
                .type('mon.doe@gmail.com')
            // alternative, imperative way of detecting that input field
            /*cy.get('.inputwrapper #email')
                .type('mon.doe@gmail.com')*/

            // submit the form on this page
            cy.get('form')
                .submit()

            // assert that the user is now logged in
            cy.get('h1')
                .should('contain.text', 'Your tasks, Mon Doe')
        })
    })

    describe('Adding a task', () => {
        it("Make sure we are in the task adding screen", () => {
            cy.get('h1')
                .should('contain.text', 'Your tasks, Mon Doe')
        })

        // see if the task specified in the fixture is added
        it('Add task', () => {
            cy.fixture('task.json')
                .then((task) => {
                    cy.get('#title')
                        .type(task.title)
                    cy.get('#url')
                        .type(task.url)
                })
            // press the button to add the task
            cy.get('input')
                .last().click()
        })

        it('Make sure the task is added', () => {
            // find the task we just added
            cy.fixture('task.json')
                .then((task) => {
                    cy.get('.title-overlay')
                        .contains(task.title)
                })
        })
    });
});

describe("user case R8UC2", () => { 
    describe('Adding items to the todo list of a task and striking them', () => {
        it('open the task and add a todo item', () => {
            cy.get(".container-element")
                .first()
                .click()
            // get the h1 in the popup div
            cy.fixture('task.json')
                .then((task) => {
                    cy.get('h1')
                        .should('contain.text', task.title)
                    
                    cy.get(".todo-item")
                        .first()
                        .contains(task.todos)
                })
            
        })

        it("Clicking the small circlue beside the todo text should strike it", () => { 
            cy.fixture('task.json')
                .then((task) => {
                    cy.get(".todo-item")
                        .first()
                        .find('.checker')
                        .click()
                        .then(() => { 
                            cy.get(".todo-item > .editable")
                                .first()
                                .should('have.css', 'text-decoration', 'line-through solid rgb(49, 46, 46)')
                        })
                })
        });

        it("Clicking the small x beside the todo text should delete it", () => {
            cy.fixture('task.json')
                .then((task) => {
                    cy.get(".todo-item")
                        .first()
                        .find('.remover')
                        .click()
                        .then(() => {
                            cy.get(".todo-item")
                                .should('not.exist')
                        })
                })
        })

    })
})
