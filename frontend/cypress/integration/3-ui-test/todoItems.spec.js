describe('R8UC1: create a ToDo item', () => { 
    describe('User should be logged in', () => {
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
        it('User should have atleast one task', () => {
            cy.contains('div', 'Email Address')
                .find('input[type=text]')
                .type('mon.doe@gmail.com')
            // alternative, imperative way of detecting that input field
            /*cy.get('.inputwrapper #email')
                .type('mon.doe@gmail.com')*/

            // submit the form on this page
            cy.get('form')
                .submit()
            
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
            
            cy.fixture('task.json')
            .then((task) => {
                cy.get('.title-overlay')
                    .contains(task.title)
            })

            cy.get('.title-overlay').click()
        })

        it('TC1: When a user enters text into textfield and presses add, new todo should be created', () => { 
            cy.get('.inline-form')
                .find('input[type=text]')
                .type('Hello world')

            cy.get('.inline-form')
            .find('input[type=submit]')
                .click()
            
            cy.get('.todo-list > :nth-child(2) > .editable').contains('Hello world')
        })

        it('TC2: If the text field is left empty then the todo should not be added when the user clicks add & textfield should get red border', () => { 
            cy.get('.inline-form')
                .find('input[type=submit]')
                .click()
            
            cy.get('.inline-form')
                .find('input[type=text]')
                .should('have.class', 'error')
        })

        it('logout', () => { 
            cy.get(".close-btn").click()
            cy.get(".navbar>.navbar-nav>.nav-item").click()
            cy.get(".menu-item").click()
            cy.get(".navbar>.navbar-nav>.nav-item").click()

        })
    })
})

describe('R8UC2: marking todo items as done', () => { 
    it('login', () => {
        cy.contains('div', 'Email Address')
            .find('input[type=text]')
            .type('mon.doe@gmail.com')
        // alternative, imperative way of detecting that input field
        /*cy.get('.inputwrapper #email')
            .type('mon.doe@gmail.com')*/

        // submit the form on this page
        cy.get('form')
            .submit()
        
        cy.fixture('task.json')
        .then((task) => {
            cy.get('.title-overlay')
                .contains(task.title)
        })

        cy.get('.title-overlay').click()
    });

    it('TC1: Clicking icon before the todo item should mark the todo item as done with line threw', () => {
        cy.get('.todo-list')
            .get('.todo-item')
            .first()
            .find('.checker')
            .click()
        
        // the .checker should now also have a secondary class of checked
        cy.get('.todo-list')
            .get('.todo-item')
            .first()
            .find('.checker')  
            .should('have.class', 'checked')
    })

    it('TC2: Clicking the icon again should make todo unDone', () => { 
        cy.get('.todo-list')
            .get('.todo-item')
            .first()
            .find('.checker')
            .click()
        
        // the .checker should now also have a secondary class of checked
        cy.get('.todo-list')
            .get('.todo-item')
            .first()
            .find('.checker')  
            .should('have.class', 'unchecked')
    })
    it('logout', () => { 
        cy.get(".close-btn").click()
        cy.get(".navbar>.navbar-nav>.nav-item").click()
        cy.get(".menu-item").click()
        cy.get(".navbar>.navbar-nav>.nav-item").click()

    })
})

describe('R8UC3: deleting todo items', () => { 
    it('login', () => {
        cy.contains('div', 'Email Address')
            .find('input[type=text]')
            .type('mon.doe@gmail.com')
        // alternative, imperative way of detecting that input field
        /*cy.get('.inputwrapper #email')
            .type('mon.doe@gmail.com')*/

        // submit the form on this page
        cy.get('form')
            .submit()
        
        cy.fixture('task.json')
        .then((task) => {
            cy.get('.title-overlay')
                .contains(task.title)
        })

        cy.get('.title-overlay').click()
    });
    it('TC1: Clicking on the "x" beside the todo item should remove it from the list', () => {
        
        cy.get('.todo-list > :nth-child(2) > .remover').click().click()
        
        // no elements with hello world should be found
        cy.get('.todo-list')
            .get('.todo-item')
            .contains('Hello world')
            .should('not.exist')
    })
})