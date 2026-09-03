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
                        <td>${contact.phone}</td>
                        <td>${contact.email || ""}</td>
                        <td>${contact.address || ""}</td>
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