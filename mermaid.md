%%{init: {'theme': 'default', 'themeVariables': { 'fontSize': '26px', 'fontFamily': 'Arial'}}}%%
sequenceDiagram
    participant User
    participant PaymentForm as Sandbox Payment Form
    participant MockTx as Mock Transaction Generator
    participant DB as Database
    participant Ticket as Ticket Generator

    User->>PaymentForm: Enter details & confirm payment
    PaymentForm->>MockTx: Send sandbox payment request
    MockTx-->>PaymentForm: Return mock transaction result
    alt Payment Successful
        PaymentForm->>DB: Store payment & booking info
        DB-->>PaymentForm: Confirm saved
        PaymentForm->>Ticket: Generate ticket
        Ticket-->>User: Show downloadable ticket
    else Payment Failed
        PaymentForm-->>User: Display failure message
    end
