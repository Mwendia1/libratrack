import { useState } from "react";
const BACKEND = "http://127.0.0.1:8000";

export default function Register() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  function submit(e) {
    e.preventDefault();
    fetch(`${BACKEND}/members`, {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({ name, email })
    })
      .then(r => {
        if (!r.ok) return r.json().then(j => Promise.reject(j));
        return r.json();
      })
      .then(() => {
        alert("Member created");
        setName(""); setEmail("");
      })
      .catch(err => alert(err.detail || JSON.stringify(err)));
  }

  return (
    <div style={{ padding: 20 }}>
      <h2>Register Member</h2>
      <form onSubmit={submit}>
        <div>
          <input placeholder="Name" value={name} onChange={e=>setName(e.target.value)} />
        </div>
        <div>
          <input placeholder="Email (optional)" value={email} onChange={e=>setEmail(e.target.value)} />
        </div>
        <button type="submit">Register</button>
      </form>
    </div>
  );
}
