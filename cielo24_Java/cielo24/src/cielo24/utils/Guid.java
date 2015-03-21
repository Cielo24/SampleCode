package cielo24.utils;

import java.util.UUID;

public class Guid {

    private UUID uuid;

    public Guid(String g){
        String uuidFormatted = g.substring(0, 8) + "-" +
                               g.substring(8, 12) + "-" +
                               g.substring(12, 16) + "-" +
                               g.substring(16, 20) + "-" +
                               g.substring(20, 32);
        this.uuid = UUID.fromString(uuidFormatted);
    }

    public boolean equals(Guid other) {
        return this.uuid.equals(other.uuid);
    }

    public UUID toUUID() {
        return this.uuid;
    }

    public String toString() {
        return this.uuid.toString().replaceAll("-", "");
    }
}