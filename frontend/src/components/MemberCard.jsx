function MemberCard({ member }) {
  return (
    <div style={{ border: "1px solid #ccc", padding: "10px", marginTop: "10px" }}>
      <h3>{member.name}</h3>
      <p>ID: {member.id}</p>
    </div>
  );
}

export default MemberCard;
