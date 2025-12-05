import { useState } from "react";

function Register() {
  const [name, setName] = useState("");

  function handleSubmit(e) {
    e.preventDefault();

    fetch("http://127.0.0.1:8000/members", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name }),
    });

    alert("Member Registered!");
    setName("");
  }

  return (
    <div style={{ padding: "20px" }}>
      <h2>Register Member</h2>

      <form onSubmit={handleSubmit}>
        <input
          value={name}
          placeholder="Enter member name"
          onChange={e => setName(e.target.value)}
        />

        <button type="submit">Register</button>
      </form>
    </div>
  );
}

export default Register;
