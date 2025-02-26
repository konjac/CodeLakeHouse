package org.konjac;

import com.microsoft.sqlserver.jdbc.SQLServerAccessTokenCallback;
import com.microsoft.sqlserver.jdbc.SqlAuthenticationToken;

public class TokenLibraryCallback implements SQLServerAccessTokenCallback {
    @Override
    public SqlAuthenticationToken getAccessToken(String spn, String stsurl) {
        String accessToken = mssparkutils.credentialsJ.getToken("DW", "");
        return new SqlAuthenticationToken(accessToken, System.currentTimeMillis() + 1800000);
    }
}