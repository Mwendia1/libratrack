import { useEffect, useState } from "react";
import MemberCard from "../components/MemberCard";

function Members() {
  const [members, setMembers] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/members")
      .then(res => res.json())
      .then(data => setMembers(data));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2>Members</h2>
      {members.map(member => (
        <MemberCard key={member.id} member={member} />
      ))}
    </div>
  );
}

export default Members;
