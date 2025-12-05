import { useEffect, useState } from "react";
import MemberCard from "../components/MemberCard";

const BACKEND = "http://127.0.0.1:8000";

export default function Members() {
  const [members, setMembers] = useState([]);

  useEffect(() => {
    fetch(`${BACKEND}/members`).then(r => r.json()).then(setMembers).catch(console.error);
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h2>Members</h2>
      {members.map(m => <MemberCard key={m.id} member={m} />)}
    </div>
  );
}
