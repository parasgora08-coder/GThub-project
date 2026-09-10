function searchContacts() {

    let query = document.getElementById("searchInput").value;

    fetch("/search?q=" + encodeURIComponent(query))
        .then(response => response.json())
        .then(data => {

            let table = document.getElementById("contactTable");

            table.innerHTML = "";

            data.forEach(contact => {

                let row = `
                    <tr>
                        <td>${contact.id}</td>
                        <td>${contact.name}</td>
                        <td>${contact.nickname || ""}</td>
                        <td>${contact.phone}</td>
                        <td>${contact.phone_type || 'Mobile'}</td>
                        <td>${contact.alternate_phone || ""}</td>
                        <td>${contact.email || ""}</td>
                        <td>${contact.city || ""}</td>
                        <td>${contact.country || ""}</td>
                        <td>${contact.company || ""}</td>
                        <td>${contact.department || ""}</td>
                        <td>${contact.job_title || ""}</td>
                        <td>${contact.birth_date || ""}</td>
                        <td>${contact.website ? `<a href="${contact.website}" target="_blank">${contact.website}</a>` : ""}</td>
                        <td>${contact.linkedin ? `<a href="${contact.linkedin}" target="_blank">${contact.linkedin}</a>` : ""}</td>
                        <td>${contact.preferred_contact || 'Phone'}</td>
                        <td>${contact.category || ""}</td>
                        <td>${contact.notes || ""}</td>
                        <td>
                            <a
                                href="/delete/${contact.id}"
                                class="delete-btn"
                                onclick="return confirm('Delete this contact?')"
                            >
                                Delete
                            </a>
                        </td>
                    </tr>
                `;

                table.innerHTML += row;
            });
        });
}